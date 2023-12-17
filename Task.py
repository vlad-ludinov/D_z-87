from pyDatalog import pyDatalog


pyDatalog.create_terms('sum_arrays, N1, N, Sum1, Sum')

+ sum_arrays([], 0)

sum_arrays([N1 | N], Sum1) <= (sum_arrays(N, Sum)) & (Sum1 == N1 + Sum)

print(sum_arrays([1, 2, 3], Sum1))