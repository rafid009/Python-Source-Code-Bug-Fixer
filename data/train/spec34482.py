import numpy as np 

def function(x):

	t3 = x
	v0 = x
	x = x
	paths = []
	try:
		if x >= 6:
			t3 = t3+t3
			paths.append(1)
		else:
			t3 = 2*t3
			paths.append(2)
		if t3 <= 2:
			v0 = v0/7
			paths.append(3)
		else:
			x = x*x
			x = 0-2
			paths.append(4)
		paths.append(5)
		assert v0 >= 0
		v0 = v0**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))