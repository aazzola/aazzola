---
title: "Automate SVN/Git Backups of Entire Salesforce.com Organizations"
type: post
draft: false
date: 2013-10-17T00:00:00
---
# Automate SVN/Git Backups of Entire Salesforce.com Organizations

[Andrea Azzola](../index.html "Back to the Home Page")


Posted on
2013-10-17 10:36
\[<a href="index.html" target="_self" title="Permalink to Automate SVN/Git Backups of Entire Salesforce.com Organizations">Permalink</a>\]

The following solution involves two popolar SCM (SVN and Git), an always-on server (I use *Windows*, you may want to opt for the cloud) and a few free tools. You will need the *Force.com Migration Tool*, *Apache Ant*, and *Java JDK*. Start by setting things up with the following checklist:

1.  Java JDK - <http://www.oracle.com/technetwork/java/javase/downloads/index.html>
2.  Apache Ant - <http://ant.apache.org/manual/install.html>
3.  Force.com Migration Tool - <http://www.salesforce.com/us/developer/docs/daas/Content/forcemigrationtool_install.htm>
4.  Shell (or the Git Bash) - <http://cygwin.com/install.html>

I'm using SVN, so an SVN command line client that support the server version (which is above 1.7) is also necessary.

1.  SVN Client - <http://www.sliksvn.com/en/download>

The next things is setting up working folder and scripts, you'll have:

    myWorkingFolder
      build.properties - Connection info
      build.xml - Retrieve instructions
      myScript.sh

**build.properties** content:

    # build.properties

    sf.serverurl = https://www.salesforce.com
    sf.username = usr@domain.ext
    sf.password = F4ncy!Pwd
    sf.directory = Org

**build.xml** content:

        <target name="getOrg">
          <mkdir dir="Org"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="AccountCriteriaBasedSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="AccountOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="ApexClass"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="ApexComponent"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="ApexPage"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="ApexTrigger"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="AssignmentRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CallCenter"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="CampaignCriteriaBasedSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CampaignOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CaseCriteriaBasedSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CaseOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Community"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="ContactCriteriaBasedSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="ContactOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomApplication"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomApplicationComponent"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomLabels"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomObject"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="CustomObjectOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomObjectTranslation"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomPageWebLink"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomSite"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="CustomTab"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Dashboard"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Document"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="EmailTemplate"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Flow"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Group"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="HomePageComponent"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="HomePageLayout"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Layout"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="LeadCriteriaBasedSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="LeadOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Letterhead"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="OpportunityCriteriaBasedSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}"
                    metadataType="OpportunityOwnerSharingRule"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="PermissionSet"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Portal"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Profile"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Queue"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="RemoteSiteSetting"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Report"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="ReportType"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Role"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Scontrol"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="StaticResource"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Workflow"
                    retrieveTarget="${sf.directory}"/>
            <sf:bulkRetrieve  username="${sf.username}" password="${sf.password}"
                    serverurl="${sf.serverurl}" metadataType="Settings"
                    retrieveTarget="${sf.directory}"/>
        </target>
    </project>

**run.cmd** content:

    svn checkout https://localhost:81/svn/myorg/trunk/ Org --depth=infinity --username bot
                    --password POOr+9jC --non-interactive --trust-server-cert
    call ant getOrg
    cd Org
    svn propedit svn:ignore *.xml .
    svn add --depth=infinity *
    svn commit -m "Scheduled commit" --username bot --password B0tP4$$:)

Open the bash, run the the scripts, the results should be the following:

    myWorkingFolder/
      myOrg/ - Project
      myOrg/.svn - SVN stuff (or .git for git stuff)
      myOrg/*.* - Versioned metadata

If you want to schedule the script in Windows, all you need to do is open the *command prompt*; and run the bash executable passing the script path as parameter, note that the whole process takes place in the working directory.

**Please note:** the script is for demonstration purpose only and comes with no guarantees. Also, this may be out of date or I could have made mistakes Please leave a comment below and I'll be happy to fix it for you.

Categories:

Share on:
<a href="https://twitter.com/intent/tweet?text=Automate%20SVN/Git%20Backups%20of%20Entire%20Salesforce.com%20Organizations&amp;url=http%3a%2f%2fandreaazzola.com%2fsalesforce-backup-organization-svn-git%2f" target="_blank" title="Share it on Twitter">Twitter</a>, 
<a href="http://facebook.com/sharer.php?u=http%3a%2f%2fandreaazzola.com%2fsalesforce-backup-organization-svn-git%2f" target="_blank" title="Share it on Facebook">Facebook</a>
<a href="https://AndreaAzzola.com" rel="author"></a>

### Comments

<a href="javascript:__doPostBack(&#39;ctl00$cphBody$cmm$lbtNewComment1&#39;,&#39;&#39;)" id="ctl00_cphBody_cmm_lbtNewComment1" class="action">Post a new comment</a>

Author's portrait

<a href="http://twitter.com/AndreaAzzola" rel="me" target="_blank" data-text="Twitter" title="Stay up to date with my tweets">My Twitter profile</a><a href="http://www.linkedin.com/in/andreaazzola" rel="me" target="_blank" data-text="LinkedIn" title="Find me on LinkedIn">My LinkedIn profile</a><a href="http://www.facebook.com/andrea.azzola" rel="me" target="_blank" data-text="Facebook" title="Get in touch with Facebook">My Facebook profile</a><a href="http://www.pinterest.com/andreaazzola" rel="me" target="_blank" data-text="Pinterest" title="I&#39;m on Pinterest!">My Pinterest profile</a><a href="http://instagram.com/andrea.azzola" rel="me" target="_blank" data-text="Instagram" title="My Instagram profile">My Instagram profile</a>

- <a href="../about/index.html" style="font-weight:bold" data-text="About" title="Short summary">About</a>
- <a href="../articles/index.html" style="font-weight:bold" data-text="Articles" title="Collection of all articles in this website">Articles</a>
- <a href="../books/index.html" style="font-weight:bold" data-text="Books" title="My book recommendations">Books</a>
- <a href="../contact/index.html" style="font-weight:bold" data-text="Contact" title="Short summary">Contact</a>
- <a href="../feed/index.html" data-text="RSS feed" title="Subscribe to this blog">RSS feed</a>
- <a href="../login/index.html" data-text="Login" title="Login">Login</a>

- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageEN%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageEN" class="lang-sm lang-lbl" lang="en"></a>
- <a href="javascript:WebForm_DoPostBackWithOptions(new%20WebForm_PostBackOptions(%22ctl00$stp1$lbLanguageIT%22,%20%22%22,%20true,%20%22%22,%20%22%22,%20false,%20true))" id="ctl00_stp1_lbLanguageIT" class="lang-sm lang-lbl" lang="it"></a>

#### Newsletter

 
 

<a href="../category/books/index.html" class="category" style="font-size:112%;">Books</a>
<a href="../category/decision-fatigue/index.html" class="category" style="font-size:112%;">Decision Fatigue</a>
<a href="../category/diet/index.html" class="category" style="font-size:112%;">Diet</a>
<a href="../category/extreme-saving/index.html" class="category" style="font-size:119%;">Extreme Saving</a>
<a href="../category/finance/index.html" class="category" style="font-size:112%;">Finance</a>
<a href="../category/financial-independence/index.html" class="category" style="font-size:125%;">Financial Independence</a>
<a href="../category/fitness/index.html" class="category" style="font-size:119%;">Fitness</a>
<a href="../category/gears/index.html" class="category" style="font-size:112%;">Gears</a>
<a href="../category/geo-arbitrage/index.html" class="category" style="font-size:112%;">Geo Arbitrage</a>
<a href="../category/goal-setting/index.html" class="category" style="font-size:112%;">Goal Setting</a>
<a href="../category/nutrition/index.html" class="category" style="font-size:112%;">Nutrition</a>
<a href="../category/personal-branding/index.html" class="category" style="font-size:112%;">Personal Branding</a>
<a href="../category/personal-development/index.html" class="category" style="font-size:150%;">Personal Development</a>
<a href="../category/productivity/index.html" class="category" style="font-size:125%;">Productivity</a>
<a href="../category/time-management/index.html" class="category" style="font-size:106%;">Time Management</a>