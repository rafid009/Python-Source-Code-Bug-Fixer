import numpy as np 

def function(x):

	f2 = 4
	j9 = x
	x = x
	paths = []
	try:
		if f2 <= 4:
			j9 = 3*j9
			x = x+3
			paths.append(1)
		else:
			x = 0+f2
			x = 4/f2
			j9 = f2-j9
			paths.append(2)
		if f2 >= 7:
			x = 5+x
			paths.append(3)
		else:
			j9 = 9+2
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