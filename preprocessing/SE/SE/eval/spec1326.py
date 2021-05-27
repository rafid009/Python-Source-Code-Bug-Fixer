import numpy as np 

def function(x):

	r0 = 2
	t3 = 7
	x = x
	paths = []
	try:
		if r0 < 6:
			r0 = r0/4
			t3 = r0-t3
			t3 = t3-2
			paths.append(1)
		else:
			x = 3*t3
			paths.append(2)
		if t3 > 7:
			r0 = r0*r0
			t3 = r0*r0
			r0 = r0-r0
			paths.append(3)
		else:
			x = x+r0
			t3 = t3-9
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		r0 = t3**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))