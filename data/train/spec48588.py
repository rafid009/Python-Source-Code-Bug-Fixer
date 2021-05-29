import numpy as np 

def function(x):

	k6 = 6
	f6 = 4
	x = 2
	paths = []
	try:
		if k6 > 5:
			x = x*k6
			x = x-4
			paths.append(1)
		else:
			x = x/7
			k6 = f6+f6
			k6 = 2*0
			paths.append(2)
		if x <= 9:
			f6 = 2/f6
			f6 = 8-f6
			x = 2-4
			paths.append(3)
		else:
			f6 = f6+f6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))