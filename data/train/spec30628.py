import numpy as np 

def function(x):

	i4 = x
	p7 = 3
	x = x
	paths = []
	try:
		if p7 < 6:
			i4 = 7*8
			paths.append(1)
		else:
			i4 = 5/5
			x = 4+x
			paths.append(2)
		if i4 > 4:
			p7 = p7*i4
			i4 = i4*7
			i4 = x+8
			paths.append(3)
		else:
			x = x/5
			x = 3*1
			i4 = 5/i4
			paths.append(4)
		paths.append(5)
		assert i4 >= 0
		i4 = i4**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))