# Ansible role for tests using fontconfig

Put this role in your `tests.yml` playbook. The playbook will first install
package dependencies listed on playbook on your localhost, then it will proceed
to run testing.  You can redefine the following variables:

 * **artifacts**: An artifacts directory on localhost to store logs
 * **remote_artifacts**: The directory on the system under test where the logs
   are stored. Note: if this variable is left undefined, it will default to
   `/tmp/artifacts`
 * **required_packages**: A list of prerequisite packages required by tests.
   Please note that for Atomic Host, additional packages will be installed
   using the `rpm-ostree` command which is affecting the test subject (it's
   similar as rebuilding an rpm package to be tested) so this should be used
   with caution on only when necessary.
 * **path_prefix**: The directory on the system where fonts are installed.
   please use one in coverage sub-parameter if having different path_prefix
   per sub-packages.
 * **package**: The package name to test. this is used to find out fontconfig
   config file. please use one in families sub-parameter if having different
   config files per sub-packages.
 * **coverage**: A list of languages for language coverage tests.
 * **families**: A list of family test cases.

## Language coverage test parameters

Supporting two types of formats. one is a simple list of languages:

    coverage:
      - en
      - fr

Another one is a dictionary that has a language as a key and values as parameters:

    coverage:
      en:
        ...
      fr:
        ...

You can redefine the following variables for dictionary format:

 * **exclude**: A list of font file names to exclude on this testing. this is
   useful to avoid unexpected failures on iterating tests when a package has
   multiple font files and has different coverages but you need to prevent
   testing for few fonts which has different coverages to them.
   Please note that the file name is relative to `path_prefix` parameter. also
   good to consider using `include` if non-targeted files is more than targeted.
 * **include**: A list of font file names to include on this testing. this is
   useful to avoid unexpected failures on iterating tests when a pcakge has
   multiple font files and has different coverages but you need to prevent
   testing for few fonts which has different coverages to them.
   Please note that the file name is relative to `path_prefix` parameter. also
   good to consider using `exclude` if targeted files is more than non-targeted.
 * **name**: The name to store logs. the test script is trying to make an unique
   file names to store logs but not perfectly working in some cases. this is
   optional parameter to make it unique by yourself.
 * **path_prefix**: A list of directory names where fonts are installed on system.
   this is optional parameter and tries to obtain the font paths from installed
   packages by `required_packages` if not available.

## Family test parameters

 * **lang**: A language to test family name for.
 * **alias**: An alias name to test.
 * **family**: A family name to test, which is supposed to be assinged to the alias.
 * **package**: The package name to test. this is used to find out fontconfig
   config file. this is optional. if not specified here, global `package`
   parameter will be used.
