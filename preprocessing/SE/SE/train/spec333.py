import numpy as np 

def function(x):

	v9 = 1
	t4 = 3
	paths = []
	try:
		if t4 > 3:
			x = v9-v9
			t4 = 1*1
			paths.append(1)
		else:
			t4 = t4+6
			x = x/4
			x = 9+x
			paths.append(2)
		if v9 >= 4:
			t4 = t4-5
			x = 7*3
			t4 = 1/t4
			paths.append(3)
		else:
			v9 = x*2
			paths.append(4)
		paths.append(5)
		assert v9 >= 0
		t4 = v9**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))