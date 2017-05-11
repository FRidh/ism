{ buildPythonPackage
, cython
, pytest
, geometry
, numpy
, matplotlib
, cytoolz
}:

buildPythonPackage rec {
  name = "ism-${version}";
  version = "0.1dev";

  src = ./.;

  checkPhase = ''
    py.test
  '';

  doCheck = false;

  buildInputs = [ cython pytest ];
  propagatedBuildInputs = [ geometry numpy matplotlib cytoolz];

}
