import numpy as np 

def function(x):

	j9 = 8
	b3 = x
	paths = []
	try:
		if j9 <= 3:
			x = 0*0
			b3 = 3+0
			x = x-6
			paths.append(1)
		else:
			j9 = j9+1
			paths.append(2)
		if b3 < 8:
			x = x*5
			x = b3*8
			paths.append(3)
		else:
			j9 = j9/j9
			b3 = b3/b3
			b3 = b3*j9
			paths.append(4)
		paths.append(5)
		assert b3 >= 0
		b3 = b3**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))