import numpy as np 

def function(x):

	u8 = 7
	n2 = x
	paths = []
	try:
		if x > 3:
			x = x/9
			n2 = 5/n2
			paths.append(1)
		else:
			u8 = x*n2
			n2 = 2+n2
			paths.append(2)
		if x <= 8:
			n2 = u8*0
			x = 6+x
			paths.append(3)
		else:
			n2 = n2/7
			n2 = 7+n2
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