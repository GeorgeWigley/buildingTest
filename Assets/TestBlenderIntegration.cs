using System;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;
using UnityEditor;
using UnityEngine;
using UnityEngine.UI;
using Debug = UnityEngine.Debug;
using Siccity.GLTFUtility;

public class TestBlenderIntegration : EditorWindow
{
    String blenderPath = "C:/Program Files/Blender Foundation/Blender 3.4/blender.exe";
    String blenderArgs =
        "C:/Users/George.000/Desktop/blenderTest/pyTest.blend -b --python C:/Users/George.000/Desktop/blenderTest/pythonScript.py";

    // Add menu named "My Window" to the Window menu
    [MenuItem("Window/test blender")]
    static void Init()
    {
        // Get existing open window or if none, make a new one:
        TestBlenderIntegration window = (TestBlenderIntegration) EditorWindow.GetWindow(typeof(TestBlenderIntegration));
        window.Show();
    }

    void OnGUI()
    {
        if (GUILayout.Button("run blender integration"))
        {
            RunBlenderIntegration();
        }
        if (GUILayout.Button("instantiate result"))
        {
            InstantiateResultOfBlender();
        }
    }

    void RunBlenderIntegration()
    {
        Debug.Log("running blender integration");
        ProcessStartInfo processStart = new ProcessStartInfo(blenderPath, blenderArgs);
        processStart.UseShellExecute = false;
        processStart.CreateNoWindow = true;
        
        var process = Process.Start(processStart);
        
        process.WaitForExit();
        process.Close();
        Debug.Log("blender integration done");
    }

    void InstantiateResultOfBlender()
    {
        Debug.Log("importing asset");
        GameObject result = Importer.LoadFromFile("C:/Users/George.000/Desktop/blenderTest/outputs/test.gltf");
    }
}