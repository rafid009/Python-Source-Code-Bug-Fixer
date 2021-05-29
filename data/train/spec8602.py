import numpy as np 

def function(x):

	k9 = 5
	r2 = x
	paths = []
	try:
		if x > 0:
			r2 = 5-r2
			x = 1+x
			paths.append(1)
		else:
			x = x*6
			x = r2+x
			r2 = 4+x
			paths.append(2)
		if x <= 2:
			r2 = r2*0
			r2 = r2+4
			paths.append(3)
		else:
			x = r2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))