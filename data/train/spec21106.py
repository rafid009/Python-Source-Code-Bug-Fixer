import numpy as np 

def function(x):

	r6 = x
	t1 = x
	paths = []
	try:
		if t1 <= 0:
			x = x+x
			x = x/4
			paths.append(1)
		else:
			x = x/x
			x = x*x
			x = x*t1
			paths.append(2)
		if t1 > 2:
			x = x/r6
			paths.append(3)
		else:
			t1 = t1/5
			r6 = t1+2
			r6 = x/1
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		x = r6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))