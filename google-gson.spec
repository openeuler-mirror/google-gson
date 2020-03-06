Name:           google-gson
Version:        2.8.2
Release:        3
Summary:        A Java library that can be used to convert Java Objects into their JSON representation
License:        ASL 2.0
URL:            https://github.com/google/gson
Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local, mvn(junit:junit), mvn(org.apache.felix:maven-bundle-plugin), mvn(org.sonatype.oss:oss-parent:pom:)
Provides:       %{name}-javadoc%{?_isa} %{name}-javadoc
Obsoletes:      %{name}-javadoc

%description
Gson is a Java library that can be used to convert a Java object into its JSON representation.
It can also be used to convert a JSON string into an equivalent Java object. Gson can work with
arbitrary Java objects including pre-existing objects that you do not have source-code of.
There are a few open-source projects that can convert Java objects to JSON. However, most of them
require that you place Java annotations in your classes; something that you can not do if you do
not have access to the source-code. Most also do not fully support the use of Java Generics.
Gson considers both of these as very important design goals.

%prep
%autosetup -n gson-gson-parent-%{version} -p1

%pom_remove_plugin :bnd-maven-plugin gson
%pom_xpath_inject \
 "pom:plugin[pom:artifactId='maven-bundle-plugin']" \
 "<configuration>
    <instructions>
      <_include>
        bnd.bnd
      </_include>
    </instructions>
  </configuration>
  <executions>
    <execution>
      <id>
        create-manifest
      </id>
      <phase>
        process-classes
      </phase>
      <goals>
        <goal>
          manifest
        </goal>
      </goals>
    </execution>
  </executions>" gson

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md UserGuide.md
%{_javadocdir}/%{name}/*

%changelog
* Sat Dec 7 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.8.2-3
- Package init
