model Example
  parameter Real k = -1.0;
  output Real x;
  input Real u(min = -1.0, max = 1.0);
equation
  3600 * der(x) = k * x + u;
end Example;
