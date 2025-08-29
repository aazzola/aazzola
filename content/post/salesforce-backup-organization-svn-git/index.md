---
title: "Automate SVN/Git Backups of Entire Salesforce.com Organizations"
type: post
draft: false
date: 2013-10-17T00:00:00
categories: ["Salesforce", "Backup", "Version Control"]
tags: ["Salesforce", "SVN", "Git", "Backup", "Ant", "Automation"]
---

The following solution involves two popular SCM tools (**SVN** and **Git**), an always‑on server (I use *Windows*, but the cloud works as well) and a few free tools. You will need the **Force.com Migration Tool**, **Apache Ant**, and **Java JDK**. Start by setting things up with the following checklist:

1. [Java JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
2. [Apache Ant](http://ant.apache.org/manual/install.html)
3. [Force.com Migration Tool](http://www.salesforce.com/us/developer/docs/daas/Content/forcemigrationtool_install.htm)
4. [Cygwin Shell or Git Bash](http://cygwin.com/install.html)
5. [SVN Client](http://www.sliksvn.com/en/download) (if using SVN)

## Setup

Create a working folder and scripts:

```
myWorkingFolder/
  build.properties   # Connection info
  build.xml          # Retrieve instructions
  myScript.sh        # Automation script
```

### build.properties
```properties
sf.serverurl = https://www.salesforce.com
sf.username = usr@domain.ext
sf.password = F4ncy!Pwd
sf.directory = Org
```

### build.xml
```xml
<target name="getOrg">
  <mkdir dir="Org"/>
  <sf:bulkRetrieve username="${sf.username}" password="${sf.password}" serverurl="${sf.serverurl}" metadataType="ApexClass" retrieveTarget="${sf.directory}"/>
  <sf:bulkRetrieve username="${sf.username}" password="${sf.password}" serverurl="${sf.serverurl}" metadataType="ApexTrigger" retrieveTarget="${sf.directory}"/>
  <sf:bulkRetrieve username="${sf.username}" password="${sf.password}" serverurl="${sf.serverurl}" metadataType="ApexPage" retrieveTarget="${sf.directory}"/>
  <!-- add further metadata types as needed -->
</target>
```

### run.cmd
```bat
svn checkout https://localhost:81/svn/myorg/trunk/ Org --depth=infinity --username bot --password POOr+9jC --non-interactive --trust-server-cert
call ant getOrg
cd Org
svn propedit svn:ignore *.xml .
svn add --depth=infinity *
svn commit -m "Scheduled commit" --username bot --password B0tP4$$:)
```

Run the script in bash, and the result will be:

```
myWorkingFolder/
  myOrg/       # Project
  myOrg/.svn   # SVN data (or .git if using Git)
  myOrg/*.*    # Versioned metadata
```

If you want to schedule the script in Windows, open the command prompt and run the bash executable passing the script path as parameter. Note that the whole process takes place in the working directory.

> **Disclaimer (2025):** This script is for demonstration only and comes with no guarantees. It may be out of date with respect to current Salesforce APIs and best practices.
```