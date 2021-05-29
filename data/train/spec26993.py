import numpy as np 

def function(x):

	f4 = x
	c1 = x
	x = x
	paths = []
	try:
		if x < 4:
			f4 = c1+7
			paths.append(1)
		else:
			f4 = f4/3
			f4 = x+f4
			x = c1+1
			paths.append(2)
		if f4 > 7:
			x = 5+8
			paths.append(3)
		else:
			x = x*f4
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert c1 >= 0
		x = c1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))