import numpy as np 

def function(x):

	n8 = 7
	j5 = x
	paths = []
	try:
		if x <= 3:
			j5 = j5+x
			x = x+7
			paths.append(1)
		else:
			x = x-0
			j5 = 2-8
			n8 = x+x
			paths.append(2)
		if n8 < 4:
			x = 2+x
			paths.append(3)
		else:
			x = x/4
			n8 = 0+8
			paths.append(4)
		paths.append(5)
		assert j5 >= 0
		n8 = j5**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))