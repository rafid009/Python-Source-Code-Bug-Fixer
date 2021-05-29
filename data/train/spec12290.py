import numpy as np 

def function(x):

	v8 = x
	p9 = x
	paths = []
	try:
		if v8 <= 4:
			v8 = v8+p9
			v8 = v8-v8
			paths.append(1)
		else:
			x = x/1
			paths.append(2)
		if p9 <= 6:
			x = x+9
			paths.append(3)
		else:
			x = 5+9
			x = x+3
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		x = p9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))