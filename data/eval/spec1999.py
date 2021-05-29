import numpy as np 

def function(x):

	c3 = x
	t5 = 8
	paths = []
	try:
		if t5 >= 2:
			t5 = 5/t5
			t5 = 6/4
			paths.append(1)
		else:
			t5 = t5-1
			x = 3/t5
			paths.append(2)
		if t5 <= 8:
			x = x*0
			c3 = c3+c3
			x = x+1
			paths.append(3)
		else:
			c3 = 6+2
			t5 = t5-x
			paths.append(4)
		paths.append(5)
		assert c3 >= 0
		t5 = c3**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))