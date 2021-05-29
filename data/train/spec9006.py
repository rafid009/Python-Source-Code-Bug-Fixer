import numpy as np 

def function(x):

	o4 = 4
	t4 = x
	x = 8
	paths = []
	try:
		if x < 4:
			o4 = o4-o4
			x = 1*4
			t4 = 3+x
			paths.append(1)
		else:
			t4 = 2-t4
			paths.append(2)
		if x < 1:
			o4 = 7*o4
			t4 = 3*0
			o4 = o4+7
			paths.append(3)
		else:
			x = x/t4
			o4 = 0-o4
			t4 = x/6
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		t4 = o4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))