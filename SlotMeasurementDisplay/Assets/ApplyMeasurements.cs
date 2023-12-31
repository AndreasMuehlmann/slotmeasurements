using System;
using System.Collections;
using System.Collections.Generic;
using System.IO;
using System.Globalization;
using UnityEngine;

public class ApplyMeasurements : MonoBehaviour
{
    private string CsvFilePath = "../measurements.csv";
    private Quaternion Orientation = new Quaternion(0, 0, 0, 0);
    private Vector3 Acceleration = new Vector3(0, 0, 0);

    void SetCurrentAttributes() {
        string[] lines = File.ReadAllLines(CsvFilePath);
        string[] measurements = lines[lines.Length - 1].Split(',');
        float yaw = float.Parse(measurements[3], CultureInfo.InvariantCulture);
        float pitch = float.Parse(measurements[1], CultureInfo.InvariantCulture);
        float roll = float.Parse(measurements[2], CultureInfo.InvariantCulture);
        Orientation = Quaternion.Euler(roll, pitch, yaw);
        float accX = float.Parse(measurements[4], CultureInfo.InvariantCulture);
        float accY = float.Parse(measurements[5], CultureInfo.InvariantCulture);
        float accZ = float.Parse(measurements[6], CultureInfo.InvariantCulture);
        Acceleration = new Vector3(accX, accY, accZ);
    }

    void Start()
    {
        SetCurrentAttributes();
    }

    void Update()
    {
        SetCurrentAttributes();
        GetComponent<Rigidbody>().AddForce(Acceleration, ForceMode.Acceleration);
        transform.rotation = Orientation;
    }
}