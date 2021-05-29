import numpy as np 

def function(x):

	v8 = x
	t8 = 7
	paths = []
	try:
		if t8 < 2:
			x = x*1
			x = x*0
			paths.append(1)
		else:
			v8 = v8/t8
			paths.append(2)
		if x >= 7:
			t8 = t8*v8
			paths.append(3)
		else:
			v8 = t8*v8
			t8 = 0-x
			paths.append(4)
		paths.append(5)
		assert v8 >= 0
		v8 = v8**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))