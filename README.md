# PyLucene 9.10.0 Installation Guide on Mac

This guide provides comprehensive instructions for installing PyLucene 9.10.0 on a Mac, using JDK 11, and handling all necessary dependencies and configurations.

## Prerequisites

- **JDK Version**: 11 (OpenJDK)
- **Gradle Version**: 8.4
- **Java Version**: 11
- **PyLucene Version**: 9.10.0

> **Note**: We are using Java version 11 to maintain compatibility with Gradle 8.4. Upgrading Gradle may result in errors due to test file compatibility issues.

## Installation Steps

### 1. Download and Install JDK Version 11

Download the JDK 11 from the following link:

[OpenJDK 11 Download](https://www.openlogic.com/openjdk-downloads?page=1)

After installation, verify the Java version using:

```bash
java -version
```

### 2. Set JAVA_HOME Environment Variable

Find the path to your installed Java:

```bash
/usr/libexec/java_home -v 11
```

Update the `JAVA_HOME` environment variable:

1. Open the `~/.zshrc` file in a text editor:

    ```bash
    nano ~/.zshrc
    ```

2. Add the following line to the file:

    ```bash
    export JAVA_HOME=$(/usr/libexec/java_home -v 11)
    ```

3. Also, set the `JCC_JDK` variable:

    ```bash
    export JCC_JDK=/Library/Java/JavaVirtualMachines/openlogic-openjdk-11.jdk/Contents/Home
    ```

4. Save the file and reload the terminal configuration:

    ```bash
    source ~/.zshrc
    ```

### 3. Download and Install PyLucene 9.10.0

Download the PyLucene 9.10.0 source tarball:

[PyLucene 9.10.0 Source](https://lucene.apache.org/pylucene)

Extract the tarball and navigate to the PyLucene directory:

```bash
tar -xvzf pylucene-9.10.0-src.tar.gz
cd pylucene-9.10.0
```

### 4. Install Dependencies

#### ICU4C Library

Install the ICU4C library, which is required for PyLucene:

```bash
brew reinstall icu4c
brew link icu4c --force
```

Set the necessary environment variables:

```bash
export LDFLAGS="-L/usr/local/opt/icu4c/lib"
export CPPFLAGS="-I/usr/local/opt/icu4c/include"
echo 'export PATH="/usr/local/opt/icu4c/bin:$PATH"' >> ~/.zshrc
echo 'export PATH="/usr/local/opt/icu4c/sbin:$PATH"' >> ~/.zshrc
```

Verify the installed version of ICU4C:

```bash
ls /usr/local/Cellar/icu4c/
```

If the version is 74.2, use the following exports:

```bash
export ICU_VERSION=74.2
export PYICU_INCLUDES=/usr/local/Cellar/icu4c/74.2/include
export PYICU_LFLAGS=-L/usr/local/Cellar/icu4c/74.2/lib
```

### 5. Install PyICU and JCC

Install the PyICU and JCC Python modules:

```bash
PKG_CONFIG_PATH=/usr/local/opt/icu4c/lib/pkgconfig pip3 install pyicu
pip3 install jcc
```

### 6. Modify the Makefile

Update the following lines in the `Makefile` to ensure compatibility with your setup:

```makefile
PREFIX_PYTHON=/usr/local
PYTHON=$(PREFIX_PYTHON)/bin/python3
JCC=$(PYTHON) -m jcc
NUM_FILES=16

+MONITOR_JAR=$(LUCENE)/monitor/build/runtimeJars/lucene-monitor-$(LUCENE_VER)-SNAPSHOT.jar
+JARS+=$(MONITOR_JAR)            # monitor
```

### 7. Compile and Install PyLucene

Navigate to the directory where you extracted PyLucene and run the following commands to compile it:

```bash
make
```

If you encounter an error related to "Illegal option," ensure that the steps related to setting the environment variables and modifying the Makefile were correctly followed.

Finally, install PyLucene by running:

```bash
sudo python3 setup.py install
```

### 8. Additional Commands

For handling specific ICU4C and Java tasks, use the following commands:

- Check the path of `icupkg`:

    ```bash
    which icupkg
    ```

- Locate any references to `icupkg`:

    ```bash
    grep -r "icupkg" .
    ```

- Use `icupkg` for handling ICU data:

    ```bash
    /usr/local/opt/icu4c/sbin/icupkg --add utr30.nrm new utr30.dat
    /usr/local/opt/icu4c/sbin/icupkg --type l --add utr30.nrm new utr30.dat
    ```

- If you encounter issues with Python packages, update `setuptools`:

    ```bash
    python3 -m pip install --upgrade setuptools
    ```

    If necessary, use `easy_install`:

    ```bash
    python3 -m easy_install --always-unzip /usr/local/lib/python3.12/site-packages/lucene-9.6.0-py3.12-macosx-14.0-x86_64.egg
    ```

- Install any missing Python distribution utilities:

    ```bash
    sudo python3 -m pip install distutils
    ```

### 9. Final Steps

After completing the installation, you can now use PyLucene in your Python projects!
