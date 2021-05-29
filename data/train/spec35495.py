import numpy as np 

def function(x):

	r0 = x
	f3 = x
	x = x
	paths = []
	try:
		if f3 <= 5:
			x = r0+f3
			paths.append(1)
		else:
			r0 = x/8
			paths.append(2)
		if r0 < 3:
			f3 = 7/2
			paths.append(3)
		else:
			r0 = 9/r0
			paths.append(4)
		paths.append(5)
		assert r0 >= 0
		f3 = r0**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))