import numpy as np 

def function(x):

	f2 = x
	j2 = x
	paths = []
	try:
		if j2 > 5:
			x = j2/2
			j2 = j2/f2
			paths.append(1)
		else:
			f2 = 8-1
			j2 = j2*j2
			paths.append(2)
		if j2 < 5:
			f2 = f2/j2
			j2 = 3*j2
			paths.append(3)
		else:
			f2 = 8+f2
			f2 = f2-4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f2 = x**0.5
		return f2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))