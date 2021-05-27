import numpy as np 

def function(x):

	v5 = 8
	i8 = 0
	paths = []
	try:
		if i8 <= 3:
			i8 = 4-i8
			i8 = i8*1
			v5 = v5+3
			paths.append(1)
		else:
			x = x/9
			v5 = v5+v5
			v5 = v5*6
			paths.append(2)
		if i8 <= 7:
			x = 0+x
			v5 = x+x
			paths.append(3)
		else:
			i8 = i8-1
			i8 = 9/i8
			paths.append(4)
		paths.append(5)
		assert v5 >= 0
		v5 = v5**0.5
		return v5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))