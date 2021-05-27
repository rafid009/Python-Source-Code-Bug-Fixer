import numpy as np 

def function(x):

	p8 = x
	v5 = 0
	paths = []
	try:
		if v5 <= 5:
			v5 = v5/8
			x = 3+x
			v5 = v5-9
			paths.append(1)
		else:
			x = x+0
			x = x-p8
			paths.append(2)
		if v5 < 4:
			v5 = 7+p8
			x = p8/2
			x = x/5
			paths.append(3)
		else:
			p8 = 5-p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		v5 = p8**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))