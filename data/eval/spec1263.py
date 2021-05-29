import numpy as np 

def function(x):

	f3 = x
	r0 = x
	paths = []
	try:
		if x > 5:
			f3 = 7-f3
			r0 = r0/5
			x = 4*r0
			paths.append(1)
		else:
			r0 = r0+1
			f3 = f3*4
			paths.append(2)
		if r0 >= 2:
			x = x/5
			f3 = 1/3
			f3 = 9+f3
			paths.append(3)
		else:
			x = x+9
			f3 = 4/r0
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		r0 = f3**0.5
		return r0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))