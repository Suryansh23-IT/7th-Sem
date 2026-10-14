#ifdef _WIN32
#define API __declspec(dllexport)
#else
#define API
#endif
API double c_to_f(double c) { return c * 9.0 / 5.0 + 32.0; }
API double f_to_c(double f) { return (f - 32.0) * 5.0 / 9.0; }
