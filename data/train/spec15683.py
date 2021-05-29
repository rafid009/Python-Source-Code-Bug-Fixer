import numpy as np 

def function(x):

	f6 = 5
	j6 = x
	paths = []
	try:
		if f6 < 2:
			x = x*6
			x = 9*4
			paths.append(1)
		else:
			j6 = j6+f6
			x = x*j6
			paths.append(2)
		if f6 > 9:
			f6 = x-0
			x = x/4
			f6 = 3*0
			paths.append(3)
		else:
			j6 = 1/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))