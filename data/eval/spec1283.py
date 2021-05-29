import numpy as np 

def function(x):

	i4 = x
	u2 = x
	x = x
	paths = []
	try:
		if u2 <= 4:
			i4 = 4+i4
			u2 = u2-u2
			paths.append(1)
		else:
			i4 = i4-7
			u2 = u2+9
			u2 = 0+8
			paths.append(2)
		if i4 <= 2:
			u2 = u2*8
			u2 = 6+u2
			paths.append(3)
		else:
			i4 = i4+i4
			x = i4-6
			i4 = i4/9
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