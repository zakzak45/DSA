import java.util.*;


public class Tree {
    public TreeNode root;


    public Tree(){
        this.root =null;
    }



    //inserting a node 
  public void insert(int val) {
        TreeNode newNode = new TreeNode(val);
        
        if (root == null) {
            root = newNode;
            return;
        }

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            TreeNode current = queue.poll();

            if (current.left == null) {
                current.left = newNode;
                return;
            } else {
                queue.add(current.left);
            }

            if (current.right == null) {
                current.right = newNode;
                return;
            } else {
                queue.add(current.right);
            }
        }
    }
 }



 