import numpy as np 

def function(x):

	v3 = 5
	t0 = x
	paths = []
	try:
		if x <= 7:
			v3 = v3-8
			v3 = v3-x
			x = 4+v3
			paths.append(1)
		else:
			t0 = 1/8
			x = 8*6
			x = x+t0
			paths.append(2)
		if v3 <= 7:
			x = x/7
			x = 5+x
			paths.append(3)
		else:
			v3 = v3*1
			v3 = 6-v3
			x = 2*x
			paths.append(4)
		paths.append(5)
		assert t0 >= 0
		t0 = t0**0.5
		return t0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))