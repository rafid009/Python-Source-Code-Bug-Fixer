import numpy as np 

def function(x):

	v8 = 2
	p9 = 1
	paths = []
	try:
		if p9 < 2:
			p9 = v8+1
			v8 = v8*x
			paths.append(1)
		else:
			x = 8+x
			p9 = p9*p9
			paths.append(2)
		if v8 >= 5:
			p9 = 6/p9
			v8 = 7/7
			paths.append(3)
		else:
			v8 = v8/p9
			v8 = v8*8
			p9 = 9-0
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		x = v8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))