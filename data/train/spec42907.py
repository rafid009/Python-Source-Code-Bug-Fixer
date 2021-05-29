import numpy as np 

def function(x):

	n7 = 9
	b5 = 0
	x = 9
	paths = []
	try:
		if x > 1:
			x = 0-8
			b5 = 0+b5
			paths.append(1)
		else:
			x = 2*0
			x = 1*x
			x = 5/b5
			paths.append(2)
		if n7 <= 8:
			b5 = x/2
			b5 = b5/n7
			n7 = n7-7
			paths.append(3)
		else:
			n7 = n7/n7
			b5 = x+7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))