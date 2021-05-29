import numpy as np 

def function(x):

	b5 = x
	o3 = x
	paths = []
	try:
		if b5 >= 1:
			o3 = o3*2
			b5 = 3*b5
			b5 = b5*o3
			paths.append(1)
		else:
			x = x*1
			x = 3*9
			paths.append(2)
		if b5 < 2:
			b5 = b5-6
			x = o3*3
			x = 6+x
			paths.append(3)
		else:
			b5 = 7+4
			x = 3*8
			b5 = o3/6
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))