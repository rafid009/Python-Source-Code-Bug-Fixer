import numpy as np 

def function(x):

	r0 = x
	b0 = 8
	paths = []
	try:
		if b0 < 5:
			b0 = 5/6
			x = 4-3
			paths.append(1)
		else:
			b0 = 2-b0
			x = 8+6
			x = x/5
			paths.append(2)
		if r0 <= 2:
			x = x/1
			x = r0+x
			paths.append(3)
		else:
			r0 = 2-r0
			paths.append(4)
		paths.append(5)
		assert b0 >= 0
		b0 = b0**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))