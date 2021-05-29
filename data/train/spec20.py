import numpy as np 

def function(x):

	t3 = 4
	r2 = 1
	paths = []
	try:
		if x > 7:
			r2 = 9-3
			paths.append(1)
		else:
			r2 = r2-6
			t3 = t3/4
			t3 = t3*4
			paths.append(2)
		if t3 <= 2:
			r2 = r2/t3
			t3 = t3*t3
			r2 = 5-r2
			paths.append(3)
		else:
			x = x*1
			paths.append(4)
		paths.append(5)
		assert r2 >= 0
		r2 = r2**0.5
		return r2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))