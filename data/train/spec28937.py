import numpy as np 

def function(x):

	v2 = 6
	b3 = x
	paths = []
	try:
		if x > 9:
			x = x+8
			v2 = x*0
			x = 3+v2
			paths.append(1)
		else:
			v2 = v2-b3
			paths.append(2)
		if v2 >= 4:
			v2 = x/7
			x = 2+x
			paths.append(3)
		else:
			b3 = b3-1
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