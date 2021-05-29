import numpy as np 

def function(x):

	f0 = 3
	j8 = 7
	paths = []
	try:
		if x <= 9:
			x = 7/x
			x = x/3
			f0 = f0+2
			paths.append(1)
		else:
			x = x/f0
			j8 = j8-1
			f0 = 4*0
			paths.append(2)
		if f0 >= 0:
			f0 = f0-f0
			paths.append(3)
		else:
			f0 = 7/8
			x = 3+x
			j8 = j8*2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))