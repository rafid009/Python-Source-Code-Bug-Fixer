import numpy as np 

def function(x):

	r3 = 9
	f3 = x
	paths = []
	try:
		if x >= 6:
			x = x*f3
			f3 = f3+4
			paths.append(1)
		else:
			f3 = f3*f3
			f3 = 3-f3
			x = x+2
			paths.append(2)
		if r3 < 0:
			f3 = f3-f3
			x = x/7
			x = x/2
			paths.append(3)
		else:
			f3 = f3+1
			x = 5*f3
			x = 1+r3
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		f3 = f3**0.5
		return f3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))