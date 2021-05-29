import numpy as np 

def function(x):

	t3 = 7
	p8 = x
	paths = []
	try:
		if x < 4:
			x = x+p8
			t3 = t3*0
			t3 = 5/7
			paths.append(1)
		else:
			t3 = 3-6
			t3 = 7-t3
			x = 9-2
			paths.append(2)
		if t3 > 1:
			t3 = 5*t3
			paths.append(3)
		else:
			p8 = p8/5
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		t3 = p8**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))