import numpy as np 

def function(x):

	i6 = x
	p2 = 8
	paths = []
	try:
		if x < 3:
			p2 = 5-4
			p2 = p2/6
			paths.append(1)
		else:
			p2 = p2/3
			i6 = 2/i6
			paths.append(2)
		if x <= 1:
			i6 = i6+3
			p2 = p2-p2
			paths.append(3)
		else:
			p2 = 0/p2
			x = 9+5
			x = 8*0
			paths.append(4)
		paths.append(5)
		assert i6 >= 0
		i6 = i6**0.5
		return i6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))