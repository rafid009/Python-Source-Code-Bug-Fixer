import numpy as np 

def function(x):

	f0 = x
	j6 = x
	paths = []
	try:
		if j6 > 0:
			f0 = f0+x
			paths.append(1)
		else:
			x = x*3
			j6 = 4/9
			paths.append(2)
		if j6 <= 4:
			f0 = 2+f0
			j6 = j6+8
			j6 = x*6
			paths.append(3)
		else:
			j6 = j6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j6 = x**0.5
		return j6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))