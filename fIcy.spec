Summary:	an icecast/shoutcast stream grabber suite
Name:		fIcy
Version:	1.0.18
Release:	1
License:	GPL v2+
Group:		Applications/Networking
Source0:	http://www.thregr.org/~wavexx/software/fIcy/releases/%{name}-%{version}.tar.gz
# Source0-md5:	72a48db0116be57c2c3342d1efd5c893
URL:		http://www.thregr.org/~wavexx/software/fIcy/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fIcy is a small icecast/shoutcast stream grabber suite for use under
shell environment. Its goal is to automatically rip a stream into user
customisable files. It will work with ICY compatible streams, allowing
you to either to save the stream to disk or to pipe the output to a
media player, or even both. fIcy, among other uses, is ideal for
batch/unattended recording of radio programs and stream debugging.

The fIcy package includes: fIcy itself, a stream
separator/multiplexer, fResync, a fast MPEG-resyncing utility, fPls, a
playlist frontend for fIcy.

%prep
%setup -q

%build
%{__make} \
    CXX="%{__cxx}" \
    CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D fIcy		$RPM_BUILD_ROOT%{_bindir}/fIcy
install -D fPls		$RPM_BUILD_ROOT%{_bindir}/fPls
install -D fResync	$RPM_BUILD_ROOT%{_bindir}/fResync

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS FAQ NEWS README TODO
%attr(755,root,root) %{_bindir}/f*
