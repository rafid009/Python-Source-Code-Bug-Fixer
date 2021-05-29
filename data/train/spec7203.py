import numpy as np 

def function(x):

	d1 = 6
	b9 = x
	paths = []
	try:
		if b9 < 2:
			d1 = d1-0
			paths.append(1)
		else:
			b9 = b9-d1
			paths.append(2)
		if x > 4:
			d1 = d1+1
			d1 = 6+d1
			paths.append(3)
		else:
			d1 = d1*7
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		b9 = b9**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))