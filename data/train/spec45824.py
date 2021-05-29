import numpy as np 

def function(x):

	p2 = x
	t7 = 2
	x = 9
	paths = []
	try:
		if p2 > 4:
			x = x+7
			x = x-4
			paths.append(1)
		else:
			p2 = p2+7
			x = 1-x
			paths.append(2)
		if p2 > 5:
			x = x*p2
			p2 = x+p2
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert p2 >= 0
		t7 = p2**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))