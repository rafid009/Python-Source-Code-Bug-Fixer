import numpy as np 

def function(x):

	j2 = 9
	b8 = 4
	x = 0
	paths = []
	try:
		if b8 >= 0:
			j2 = j2+j2
			paths.append(1)
		else:
			j2 = j2/2
			paths.append(2)
		if b8 < 9:
			j2 = x+7
			x = x+x
			b8 = b8-5
			paths.append(3)
		else:
			b8 = 6-b8
			b8 = b8/5
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		b8 = b8**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))