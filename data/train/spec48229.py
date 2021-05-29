import numpy as np 

def function(x):

	n1 = x
	x6 = x
	paths = []
	try:
		if x < 3:
			x = 2+x
			x = 2/x
			x = x*0
			paths.append(1)
		else:
			n1 = 7+x6
			paths.append(2)
		if x <= 0:
			x6 = 5*2
			x6 = 5+9
			x = x-2
			paths.append(3)
		else:
			x = x6+x
			x = x*5
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x6 = n1**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))