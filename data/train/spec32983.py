import numpy as np 

def function(x):

	o2 = 5
	b9 = x
	paths = []
	try:
		if b9 > 6:
			x = x+9
			o2 = b9-1
			x = 2+x
			paths.append(1)
		else:
			x = b9+7
			o2 = b9+1
			x = x*6
			paths.append(2)
		if b9 >= 7:
			b9 = b9/o2
			b9 = b9+7
			paths.append(3)
		else:
			b9 = 2-7
			paths.append(4)
		paths.append(5)
		assert o2 >= 0
		b9 = o2**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))