import numpy as np 

def function(x):

	b4 = x
	x9 = x
	x = x
	paths = []
	try:
		if x9 > 6:
			x = x-2
			b4 = b4*0
			paths.append(1)
		else:
			b4 = 6+0
			paths.append(2)
		if b4 <= 9:
			x = x/x
			x9 = 6/x9
			paths.append(3)
		else:
			x = x9/5
			x9 = 2+x9
			paths.append(4)
		paths.append(5)
		assert x9 >= 0
		b4 = x9**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))