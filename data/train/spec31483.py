import numpy as np 

def function(x):

	f2 = 9
	j8 = 8
	paths = []
	try:
		if x < 4:
			f2 = f2/1
			paths.append(1)
		else:
			x = x+1
			f2 = f2+f2
			x = 6/2
			paths.append(2)
		if j8 >= 4:
			x = x-j8
			j8 = x*8
			paths.append(3)
		else:
			f2 = 8+f2
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		x = j8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))